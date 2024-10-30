# Music Album Project

## Overview

The Music Album Project is a web application designed to showcase music albums and artist details. This application utilizes Vue.js for the frontend and Django with Django REST Framework for the backend, enabling users to view a diverse range of albums along with artist information, genre, artwork, and pricing. The project aims to provide a seamless and intuitive user experience built with modern web technologies.

## Features

- **Album Display**: Showcases a list of music albums with detailed views.
- **Responsive Design**: Built with Tailwind CSS for a modern and adaptable look.
- **Error Handling**: Graceful fallback for missing album artwork to enhance user experience.
- **Detailed View**: Option to view more details about each album, including release dates and genre.
- **RESTful API**: Efficiently interacts with the backend to fetch album data.

## Table of Contents

- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Components](#components)
  - [AlbumCard.vue](#albumcardvue)
  - [ArtistCard.vue](#artistcardvue)
- [Contributing](#contributing)
- [License](#license)

## Technologies

- **Frontend**:
  - Vue.js
  - Tailwind CSS
- **Backend**:
  - Django
  - Django REST Framework
- **Database**:
  - SQLite (or any preferred database)
- **Build Tool**:
  - npm (Node Package Manager)

## Project Structure

```
/project-root
├── /backend
│   ├── manage.py
│   ├── /backend
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── /albums
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── serializers.py
│   └── requirements.txt
├── /frontend
│   ├── package.json
│   ├── /src
│   │   ├── /components
│   │   │   ├── AlbumCard.vue
│   │   │   ├── ArtistCard.vue
│   │   ├── App.vue
│   │   └── main.js
└── README.md
```

## Installation

### Backend Setup

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Start the Django server**:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the frontend directory**:

   ```bash
   cd frontend
   ```

2. **Install npm dependencies**:

   ```bash
   npm install
   ```

3. **Start the Vue development server**:

   ```bash
   npm run serve
   ```

## Usage

- Open your browser and navigate to `http://localhost:8080` (or the port your Vue app is running on) to view the application.
- The application fetches album data from the Django API and displays it using components such as `AlbumCard` and `ArtistCard`.

## API Endpoints

- **Get All Albums**:
  - **URL**: `/api/albums/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all albums.

- **Get Album by ID**:
  - **URL**: `/api/albums/<id>/`
  - **Method**: `GET`
  - **Description**: Retrieves details for a specific album by its ID.

## Components

### AlbumCard.vue

The `AlbumCard` component displays individual album information, including artwork, title, artist name, price, and additional details like genre, release date, and explicit content. Users can toggle details for more information.

#### Key Features
- Displays album artwork with error handling for missing images.
- Toggles between showing and hiding album details.
- Utilizes utility functions for formatting prices and dates.

### ArtistCard.vue

The `ArtistCard` component showcases individual artists, including their artwork and primary genre. It provides a concise view of the artist's name and genre.

#### Key Features
- Responsive design to adapt artist information presentation.
- Fallback image handling for missing artwork.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any changes or enhancements you would like to suggest.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
