# The Middleware — Learning Project Description

## Goal
Use the `the-middleware` Django project as a sandbox to practice core Django + Django REST
Framework (DRF) concepts: models, migrations, service layers, calling external HTTP APIs, and
building an API endpoint.

## Problem
Fetch data from two different public APIs, merge it into our own domain model, persist it, and
expose it through a single DRF endpoint.

### Source APIs (no API key required)
1. **REST Countries** (`https://restcountries.com`) — country facts: name, capital, region,
   population, flag.
2. **Open-Meteo** (`https://open-meteo.com`) — current weather, plus a free geocoding endpoint
   to resolve a capital city name into latitude/longitude.

### Domain
`CountrySnapshot` — a merged view combining a country's facts with the current weather at its
capital city.

Fields (indicative):
- `country_code` (e.g. ISO alpha-2/alpha-3)
- `name`
- `capital`
- `region`
- `population`
- `flag_url`
- `temperature`
- `weather_description` / weather code
- `fetched_at`

### Flow
1. Client calls `GET /api/countries/{code}/snapshot/`.
2. Service layer:
   - Fetches country data from REST Countries by code.
   - Resolves the capital's lat/lon via Open-Meteo's geocoding endpoint.
   - Fetches current weather from Open-Meteo using those coordinates.
   - Merges both results into a `CountrySnapshot`.
3. Result is persisted (with some notion of freshness/TTL, to practice caching + avoiding
   redundant upstream calls).
4. Endpoint returns the merged snapshot as JSON via a DRF serializer.

### Error handling considerations
- Unknown/invalid country code → 404.
- Upstream API failure/timeout → graceful error response, not a raw 500.

## Tech choices
- **Django REST Framework** for serializers, generic views, and the browsable API.
- `requests` for calling the external APIs (to be added to `requirements.txt`).
- A `CountrySnapshot` Django model to persist merged results (practising migrations).
- Service module separate from views, so the HTTP-fetch/merge logic is testable independent of
  the request/response cycle.

## What this exercises
- Django models & migrations
- Separating service/business logic from views
- Calling and merging data from multiple external APIs
- DRF serializers and generic API views
- Basic error handling for upstream/external failures

