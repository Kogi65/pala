# Pala
This is Pala, a logistics database management system which is intended for both clients and Pala employees, each user having their own portal.

## Features
The web app is intended to fulfil the following functions:
  + Storing personal details of customers as well as for employees allocated in various sections (warehouse staff, drivers, admin staff, shipment and tracking staffs),
  + Storing of commercial vehicles details and their mileage **Note: some vehicles are limited to carry only certain goods such as pharmaceutical drugs or indurstrial chemicals**,
  + Compute the weight limit of goods transported in vehicles,
  + Compute the shipping costs for goods transported based on weight and distance coverage,
  + Prohibit certaing goods from being shipped upon flagged as **under inspection** status unless authorized by admin staff such as military weaponry, illegal drugs or radioactive substances,
  + Keep an inventory of goods stored in warehouses,
  + Service maintenance schedule for the vehicles.

### Additional Info
Theme colours used are Orange *Hex:FFA500*, White *Hex:FFFFFF* and Brown *Hex:964B00*

Font used is semibold

Python 3.11 & Django 4.2 was used

MySQL was used for the web app but as a heads up, filling & querying the database is still not complete,

To add pages on the app, you can create your .html files in the templates folder to design the front-end layout and link them in urls.py as well as in views.py files

## Contributing
Contributions to the project are very welcomed 🙂. If you encounter any issues or have suggestions, kindly open an issue or submit a pull request.

## Installation
Follow the steps to run the project locally:

 Clone the repository
  >git clone https://github.com/Kogi65/pala.git

Create the virtual environment in your directory
  > python3 -m venv test

Activate the virtual environment

  For Windows:
>test\Scripts\activate

  For macOS/Linux:
>source test/bin/activate

Apply database migrations 
>python manage.py migrate

To start the server
>python manage.py runserver

and copy the localhost link to the web browser






  
  
