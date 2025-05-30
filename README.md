# Webfinger

App exposing the `/.well-known/webfinger` endpoint with OAuth issuer information.

---

## Image name

`shaban00/webfinger:latest`

---

## Features

- Serves the Webfinger endpoint at `/.well-known/webfinger`
- Returns JSON with the OAuth issuer URL and admin email
- Only allows **GET** requests on the endpoint
- Handles invalid routes gracefully with JSON error responses including HTTP method and requested URL
- Runs with Gunicorn as the production server

---

## Environment Variables

The app requires the following environment variables to be set at runtime:

| Variable          | Description                    | Example                          |
|-------------------|--------------------------------|---------------------------------|
| `OAUTH_SERVER_URL` | The OAuth issuer URL to return | `https://your-oauth-server.com` |
| `ADMIN_EMAIL`      | Admin email to identify subject | `admin@example.com`              |

---

## Pull Image from Docker Hub

```bash
docker pull shaban00/webfinger:latest
```

## Run the image

```bash
docker run -d \
  --name webfinger \
  -p 5000:5000 \
  -e OAUTH_SERVER_URL="https://your-oauth-server.com" \
  -e ADMIN_EMAIL="admin@example.com" \
  shaban00/webfinger:latest
```
