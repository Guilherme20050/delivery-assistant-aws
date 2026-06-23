def lambda_handler(event, context):
    if "item" in event:
        return {"status": "pedido válido"}
    else:
        return {"status": "pedido inválido"}
