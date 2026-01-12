from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee


class EmployeeAPITestCase(APITestCase):

    def setUp(self):
        """
        Create user and authenticate using JWT
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Get JWT token
        token_url = reverse("token_obtain_pair")
        response = self.client.post(token_url, {
            "username": "testuser",
            "password": "testpass123"
        }, format="json")

        self.assertEqual(response.status_code, 200)
        self.access_token = response.data["access"]

        # Authenticate all requests
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.employee_payload = {
            "name": "John123 Doe",
            "email": "john123@example.com",
            "department": "Engineering",
            "role": "Developer"
        }

        self.employee = Employee.objects.create(**self.employee_payload)

    # ---------------- CREATE ----------------
    def test_create_employee_success(self):
        payload = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "department": "HR",
            "role": "Manager"
        }
        response = self.client.post("/api/employees/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_duplicate_email(self):
        response = self.client.post(
            "/api/employees/",
            self.employee_payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------------- READ ----------------
    def test_list_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("results" in response.data)

    def test_retrieve_invalid_employee(self):
        response = self.client.get("/api/employees/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------------- UPDATE ----------------
    def test_update_employee(self):
        payload = {
            "name": "John Updated",
            "email": "john@example.com",
            "department": "Sales",
            "role": "Analyst"
        }
        response = self.client.put(
            f"/api/employees/{self.employee.id}/",
            payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["department"], "Sales")

    # ---------------- DELETE ----------------
    def test_delete_employee(self):
        response = self.client.delete(
            f"/api/employees/{self.employee.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # ---------------- AUTH EDGE CASE ----------------
    def test_access_without_authentication(self):
        self.client.credentials()  # Remove token
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
