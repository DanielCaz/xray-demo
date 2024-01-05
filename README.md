# X-Ray Demo

## Description

This is a demo api that includes X-Ray tracing for testing purposes.

## Usage

### Deploy

```bash
sam deploy
```

### Invoke a function locally

```bash

sam local invoke <function name> --env-vars env.json -e events/<event file>.json

```

## Resources created

- Lambda functions for CRUD operations
- DynamoDB table
- API Gateway
- IAM roles and policies
- X-Ray tracing
