# Food Ordering Application

A modern food ordering platform built with Next.js micro-frontends and FastAPI backend.

## Tech Stack

### Frontend

- Next.js 14
- TypeScript
- Tailwind CSS
- Micro-frontend architecture

### Backend

- FastAPI
- PostgreSQL 16
- Redis
- Nginx

## Prerequisites

Make sure you have the following installed:

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

## Project Structure

```
food-ordering-app/
├── frontend/
│   ├── container-app/    # Main application (Port 3000)
│   ├── restaurant-app/   # Restaurant dashboard (Port 3001) (example)
│   └── user-app/        # User dashboard (Port 3002) (examle)
├── backend/            # FastAPI backend
├── nginx/             # Nginx configuration
└── docker-compose.yml
```

## Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd food-ordering-app
```

2. Start all services using Docker:

```bash
docker-compose up --build
```

The application will be available at:

- Main App: http://localhost:3000
- Restaurant Dashboard: http://localhost:3001
- User Dashboard: http://localhost:3002
- API Documentation: http://localhost:8000/docs

## Development Setup

### Frontend Development

Each frontend app can be developed independently:

```bash
# Container App
cd frontend/container-app
npm install
npm run dev

# Restaurant App
cd frontend/restaurant-app
npm install
npm run dev

# User App
cd frontend/user-app
npm install
npm run dev
```

### Backend Development

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost/api/v1
```

### Backend (.env)

```env
DATABASE_URL=postgresql://user:password@db:5432/foodapp
SECRET_KEY=your-secret-key-here
REDIS_URL=redis://redis:6379/0
```

## Available Scripts

### Frontend

```bash
npm run dev     # Start development server
npm run build   # Build for production
npm run start   # Start production server
npm run lint    # Run ESLint
```

### Backend

```bash
uvicorn app.main:app --reload  # Start development server
pytest                         # Run tests
alembic upgrade head           # Run database migrations
```

## Docker Commands

### Start all services

```bash
docker-compose up --build
```

### Rebuild specific service

```bash
docker-compose up -d --build <service-name>
```

### View logs

```bash
docker-compose logs -f
```

### Stop all services

```bash
docker-compose down
```

### Clean start (remove volumes)

```bash
docker-compose down -v
docker-compose up --build
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Features

- Micro-frontend architecture
- Real-time order tracking
- Restaurant management dashboard
- User order management
- QR code payment integration
- Random shipper assignment

## Troubleshooting

### Port Conflicts

If you encounter port conflicts, ensure no other services are using:

- 3000 (Container App)
- 3001 (Restaurant App)
- 3002 (User App)
- 8000 (Backend)
- 5434 (PostgreSQL)
- 6379 (Redis)
- 80 (Nginx)

### Database Connection Issues

1. Check if PostgreSQL container is running:

```bash
docker-compose ps
```

2. Verify database credentials in .env file

### Frontend Not Loading

1. Check if all frontend containers are running
2. Verify Nginx configuration
3. Check container logs:

```bash
docker-compose logs container-app
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
