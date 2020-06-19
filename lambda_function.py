import json

import get_palette as gp

def lambda_handler(event, context):
    
    img = gp.get_data.get_image_b64(event['body'])

    c = gp.get_colours.kmeans(img)

    new_img = gp.create_output.create_palette_image(img, c)

    img_b64 = gp.create_output.image2b64(new_img)

    return {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {
            'content-type': 'image/png'
        },
        'body': json.dumps(img_b64)
    }