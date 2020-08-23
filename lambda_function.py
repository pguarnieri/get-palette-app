import json

from get_palette import get_data, get_colours, create_output

def lambda_handler(event, context):

    img = get_data.get_image_b64(img_b64=event['body'])

    c = get_colours.kmeans(img=img)

    img_out = create_output.create_palette_image(img=img, colours=c)

    img_b64 = create_output.image2b64(img=img_out)

    return {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'content-type': 'image/png'
        },
        'body': json.dumps(img_b64)
    }