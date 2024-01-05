# X-Ray Demo

## Description

This is a demo api that includes X-Ray tracing for testing purposes.

## Usage

### Deploy

```bash
sam deploy
```

### Invoke

#### Get all items

```bash
curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/Dev
```

#### Get item by id

```bash
curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/Dev/<id>
```

#### Create/Update item

```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/Dev -d '{ "id": "<id>", "name": "<name>" }'
```

#### Delete item

```bash
curl -X DELETE https://<api-id>.execute-api.<region>.amazonaws.com/Dev/<id>
```

## Resources created

- Lambda functions for CRUD operations
- DynamoDB table
- API Gateway
- IAM roles and policies
- X-Ray tracing
