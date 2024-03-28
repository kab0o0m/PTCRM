# Generated by Django 5.0.3 on 2024-03-28 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tutors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leads",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("client_name", models.CharField(max_length=200)),
                ("client_number", models.CharField(max_length=15)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new_case", "New Case"),
                            ("tutors_sent", "Tutors Sent"),
                            ("tutors_needed", "Tutors Needed"),
                            ("closed", "Closed"),
                            ("activate_tuition_centres", "Activate Tuition Centres"),
                            ("premium_education", "Premium Education"),
                            ("issue_cases", "Issue Cases"),
                            ("follow_up_to_close", "Follow Up to Close"),
                            ("group_chats_created", "Group Chats Created"),
                            ("awaiting_confirmation", "Awaiting Confirmation"),
                            ("incomplete", "Incomplete"),
                        ],
                        default="new_case",
                        max_length=50,
                    ),
                ),
                ("remarks", models.CharField(max_length=500)),
                ("many_tutor_link", models.CharField(max_length=500)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("last_reviewed_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TutorInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("sent_profile", "Sent Profile"),
                            ("cmi", "CMI"),
                            ("pending", "Pending"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                ("preferred_rate", models.CharField(max_length=30)),
                ("remarks", models.TextField()),
                ("timings", models.CharField(max_length=100)),
                (
                    "lead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tutors",
                        to="leads.leads",
                    ),
                ),
                (
                    "tutor",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tutor_information",
                        to="tutors.tutors",
                    ),
                ),
            ],
        ),
    ]
