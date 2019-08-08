from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
     def basic_validator(self, form):
        errors = {}
        if len(form["fname"]) < 1:
            errors["fname"] = "First Name is required"
        if len(form["lname"]) < 1:
            errors["lname"] = "Last Name is required"
        if len(form["email"]) < 1:
            errors["email"] = "Email field is required"
        if len(form["pw"]) < 8:
            errors["pw"] = "Password must be at least 8 characters"
        if form["pw"] != form["conf_pw"]:
            errors["pw_match"] = "Passwords do not match!"

        if not EMAIL_REGEX.match(form["email"]):
            errors["email_reg"] = "Invalid Email"
       
        result = self.filter(email=form["email"])
        if result:
            errors.append("Email already in use")

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



