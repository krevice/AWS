import boto3

# Define the Lambda function and its input parameters
def lambda_handler(event, context):
    # Connect to DynamoDB
    dynamodb = boto3.resource("dynamodb")

    # Retrieve the "visitor_count" table from DynamoDB
    table = dynamodb.Table("visitor_count")

    # Retrieve the current visit count from the "visitor_count" table
    response = table.get_item(Key={"id": 1})
    item = response.get("Item", {})
    visit_count = item.get("visit_count", 0)

    # Increment the visit count
    visit_count += 1

    # Update the visit count in the "visitor_count" table
    table.put_item(Item={"id": 1, "visit_count": visit_count})

    # Return the updated visit count
    # Set Access-Control-Allow-Origin header to allow cross-origin requests
    return {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": str(visit_count)
    } or {
        "statusCode": 404,
        "body": "Item not found"
    }
