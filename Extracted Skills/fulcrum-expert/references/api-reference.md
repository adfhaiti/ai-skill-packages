# Fulcrum REST API Reference

## Authentication

**API Token:** Include in every request via header or query parameter.

```
Header: X-ApiToken: your_api_token_here
  -- or --
Query: ?token=your_api_token_here
```

Generate tokens in Fulcrum account settings or organization profile. Requires Developer Pack enabled.

**Base URL:** `https://api.fulcrumapp.com`

---

## Rate Limits

- 5,000 API calls per hour per user
- 10,000 records per import batch
- 10 active webhooks per organization
- Implement exponential backoff on 429 responses

---

## Records API

### List Records
```
GET /api/v2/records.json?form_id={form_id}
```
Query parameters: `form_id` (required), `page`, `per_page`, `client_created_since`, `client_created_before`, `updated_since`

### Get Record
```
GET /api/v2/records/{record_id}.json
```

### Create Record
```
POST /api/v2/records.json
Content-Type: application/json

{
  "record": {
    "form_id": "form-uuid",
    "latitude": 18.2208,
    "longitude": -73.7539,
    "form_values": {
      "a001": "Value for field with key a001",
      "c002": {"choice_values": ["option_a"]},
      "y003": "yes"
    },
    "status": "in_progress",
    "project_id": "project-uuid",
    "assigned_to_id": "user-uuid"
  }
}
```

**Optional headers:**
- `X-SkipWorkflows: true` -- skip app workflows
- `X-SkipWebhooks: true` -- skip webhook triggers

### Update Record
```
PUT /api/v2/records/{record_id}.json
Content-Type: application/json

{
  "record": {
    "form_id": "form-uuid",
    "form_values": { ... }
  }
}
```
**Important:** Include the complete record object. Omitting fields may cause data loss.

### Delete Record
```
DELETE /api/v2/records/{record_id}.json
```
Returns HTTP 204 (No Content).

---

## Forms API

### List Forms
```
GET /api/v2/forms.json
```

### Get Form
```
GET /api/v2/forms/{form_id}.json
```
Returns complete form schema including all elements, status field, and configuration.

### Update Form
```
PUT /api/v2/forms/{form_id}.json
Content-Type: application/json

{
  "form": {
    "name": "Updated Name",
    "elements": [ ... ]
  }
}
```
**Warning:** Structural changes can cause permanent data loss. Always export data first.

### Get Form History
```
GET /api/v2/forms/{form_id}/history.json
```

---

## Batch API

For bulk operations on up to 10,000 records.

### Create Batch
```
POST /api/v2/batches.json
Content-Type: application/json

{
  "batch": {
    "operations": [
      {
        "action": "delete",
        "resource": "record",
        "form_id": "form-uuid",
        "query": "SELECT id FROM records WHERE status = 'draft'"
      }
    ],
    "start": true
  }
}
```

**Supported actions:** `delete`, `update` (project, assignee, status only)

**Filtering:** Use `query` (SQL) or `ids` (array of record IDs)

**Limitations:**
- One operation per batch (additional operations ignored)
- Up to 10,000 records
- Cannot be terminated once started

### Start Batch
```
POST /api/v2/batches/{batch_id}/start.json
```

### Get Batch Status
```
GET /api/v2/batches/{batch_id}.json
```
Returns: `pending`, `running`, `success`, or `failed` with counts.

---

## Photos API

### Upload Photo
```
POST /api/v2/photos.json
Content-Type: multipart/form-data

photo[access_key]: unique-access-key
photo[file]: (binary file data)
```

### Get Photo
```
GET /api/v2/photos/{access_key}.json
```

### Get Photo Image
```
GET /api/v2/photos/{access_key}/{size}.jpg
```
Sizes: `thumb`, `medium`, `large`, `original`

---

## Videos API

### Upload Video
```
POST /api/v2/videos.json
Content-Type: multipart/form-data

video[access_key]: unique-access-key
video[file]: (binary file data)
```

### Get Video
```
GET /api/v2/videos/{access_key}.json
```

---

## Audio API

### Upload Audio
```
POST /api/v2/audio.json
Content-Type: multipart/form-data

audio[access_key]: unique-access-key
audio[file]: (binary file data)
```

---

## Signatures API

### Get Signature
```
GET /api/v2/signatures/{access_key}.json
```

---

## Choice Lists API

Reusable choice lists shared across forms.

### List Choice Lists
```
GET /api/v2/choice_lists.json
```

### Create Choice List
```
POST /api/v2/choice_lists.json
Content-Type: application/json

{
  "choice_list": {
    "name": "Departments",
    "choices": [
      {"label": "Sud", "value": "sud"},
      {"label": "Grand'Anse", "value": "grand_anse"}
    ]
  }
}
```

### Update Choice List
```
PUT /api/v2/choice_lists/{id}.json
```

---

## Classification Sets API

Hierarchical classification systems.

### List Classification Sets
```
GET /api/v2/classification_sets.json
```

### Create/Update Classification Set
```
POST /api/v2/classification_sets.json
Content-Type: application/json

{
  "classification_set": {
    "name": "Plant Species",
    "items": [
      {
        "label": "Mango",
        "value": "mango",
        "child_classifications": [
          {"label": "Francique", "value": "francique", "child_classifications": []}
        ]
      }
    ]
  }
}
```

---

## Projects API

### List Projects
```
GET /api/v2/projects.json
```

### Create Project
```
POST /api/v2/projects.json
Content-Type: application/json

{
  "project": {
    "name": "Fond-des-Blancs Census 2026"
  }
}
```

---

## Members API

### List Members
```
GET /api/v2/memberships.json
```

---

## Webhooks

### Supported Events
- `form.create`, `form.update`, `form.delete`
- `record.create`, `record.update`, `record.delete`
- `choice_list.create`, `choice_list.update`, `choice_list.delete`
- `classification_set.create`, `classification_set.update`, `classification_set.delete`

### Create Webhook
```
POST /api/v2/webhooks.json
Content-Type: application/json

{
  "webhook": {
    "name": "Record Updates",
    "url": "https://your-server.com/webhook",
    "active": true
  }
}
```

### Webhook Payload
```json
{
  "event_id": "uuid",
  "event_type": "record.create",
  "owner_id": "organization_id",
  "data": { /* full resource object */ }
}
```

**Requirements:**
- Endpoint must return HTTP 200-207 within 20 seconds
- Failed requests retry with exponential backoff (25 attempts over ~20 days)
- Maximum 10 active webhooks per organization

### List Webhooks
```
GET /api/v2/webhooks.json
```

### Delete Webhook
```
DELETE /api/v2/webhooks/{webhook_id}.json
```

---

## Query API (SQL)

Run SQL queries against your data.

```
POST /api/v2/query.json
Content-Type: application/json
X-ApiToken: your_token

{
  "q": "SELECT _record_id, field_name FROM \"form_name\" WHERE status = 'complete' LIMIT 100",
  "format": "json"
}
```

**Formats:** `json`, `csv`, `geojson`

**Notes:**
- Table name is the form name in double quotes
- Column names are data_names
- System columns: `_record_id`, `_status`, `_latitude`, `_longitude`, `_created_at`, `_updated_at`, `_assigned_to`, `_project_name`
- Standard SQL syntax (PostgreSQL dialect)

---

## Client Libraries

### Python
```
pip install fulcrum
```
```python
from fulcrum import Fulcrum
client = Fulcrum(key='your_api_token')

# List forms
forms = client.forms.search()

# Get records
records = client.records.search(url_params={'form_id': 'form-uuid'})

# Create record
record = client.records.create({
    'record': {
        'form_id': 'form-uuid',
        'form_values': {'a001': 'value'}
    }
})
```

### JavaScript
```
npm install fulcrum-app
```
```javascript
const { Client } = require('fulcrum-app');
const client = new Client('your_api_token');

// List forms
const forms = await client.forms.all();

// Get records
const records = await client.records.all({form_id: 'form-uuid'});
```

---

## Common API Patterns

### Paginating through all records
```python
page = 1
all_records = []
while True:
    result = client.records.search(url_params={
        'form_id': form_id, 'page': page, 'per_page': 500
    })
    records = result['records']
    if not records:
        break
    all_records.extend(records)
    page += 1
```

### Syncing with webhooks
```python
# Webhook handler (Flask example)
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    payload = request.json
    event_type = payload['event_type']
    
    if event_type == 'record.create':
        process_new_record(payload['data'])
    elif event_type == 'record.update':
        process_updated_record(payload['data'])
    
    return '', 200  # Must return 200-207 within 20 seconds
```

### Bulk export with Query API
```python
import requests

response = requests.post(
    'https://api.fulcrumapp.com/api/v2/query.json',
    headers={
        'X-ApiToken': 'your_token',
        'Content-Type': 'application/json'
    },
    json={
        'q': 'SELECT * FROM "My Survey" WHERE _status = \'complete\'',
        'format': 'csv'
    }
)

with open('export.csv', 'w') as f:
    f.write(response.text)
```
