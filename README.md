
# Cityxa - Real Estate Django Website

This is a Django-based real estate website designed to showcase properties for sale or rent.<br/>
It allows users to search for properties/houses using various filters like location, price, number of bedrooms, property type, superficie and more. The project includes two applications: one for managing user accounts and another for managing properties. I also created a DJango rest API, to facilitate the extraction of the houses/appartments data with all their fields are easily shared.
<br/>
I use Google API for maps display and real adress, places search on globe.
</br>
I invite you to watch the short video I added above to see more options and possibilities of the website. 


https://user-images.githubusercontent.com/56579257/227270258-c950c6a6-d273-4459-9604-55818732a9c5.mp4


### Technologies:
- Python 3.9
- Django 4.1.7 + djangorestframework 3.14.0
- Postgresql as Database server
- Html+Css
- Javascript

### Features:
The website includes the following features:

- User authentication and authorization for secure access
- User roles management with different levels of access
- Integration of Google Maps API for displaying properties locations on map
- Search function to filter properties based on various criteria
- PostgreSQL database to store property, users informations and photos descriptions
- Static files for website styling
- Forms for adding, updating, and deleting properties and users using CRUD operations
- Django rest framework API, to GET the properties/houses that users published with all their fields.

### Installation:

1. Clone the project
2. Install all dependencies
3. Install PostgreSQL
4. Run Migrations
5. Get a google api key for maps display, and add it on: ..\Cityxa\src\env  
6. Run server


