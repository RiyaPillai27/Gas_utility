                                                       Gas Utility Customer Service Application
                                                       ========================================
Overview
========
This Django application provides consumer services for gas utilities, allowing customers to submit service requests online, 
track the status of their requests, and view their account information.

Getting Started
----------------
Prerequisites
=============
->XAMPP with MySQL
->Python (3.x recommended)
->Django

Installation
=============
->Install XAMPP: Download and install XAMPP from here.
->Start MySQL Server: Launch XAMPP control panel and start the MySQL server.
->Clone the repository:   git clone <repository_url>
						
->Navigate to the project directory:  cd gas_utility
									
->Install dependencies:  pip install -r requirements.txt
						
->Configure database settings:   Open gas_utility/settings.py and update the DATABASES setting to use MySQL with XAMPP.
							 
->Apply migrations:  python manage.py migrate
					

Usage
======
->Start the Django development server:  python manage.py runserver
										
->Access the application in your web browser at http://localhost:8000/.

Adding Data
===========
->To add customer data, use Django admin:   python manage.py createsuperuser

->Access the admin interface at http://localhost:8000/admin/ and log in with superuser credentials.
->To submit service requests, go to the "Submit Request" page in your browser and fill out the form.

Workflow
========
Home:
-----
	 View all service requests submitted by customers.
	 Each request displays basic information like the type of request and its status.
Submit Request:
---------------
			   Fill out the form with the type of request, details, and attachments to submit a new service request.
Track Request:
--------------
              Enter the request ID to track the status of a specific service request.
              View details such as the status, submission date, and resolution date (if resolved).

Deployment
==========
->For deployment to a production server, configure your server environment and settings appropriately.
->Set up a MySQL database, configure static files, and serve the application using a web server like Nginx or Apache.