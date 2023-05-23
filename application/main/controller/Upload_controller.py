from flask import request
from flask_restx import Resource
from ..service.Image_service import Image_service
from ..model.DTO.Upload_DTO import Upload_DTO
import base64

dto = Upload_DTO()

api = dto.api
upload_dto = dto.upload_dto
upload_parser = api.parser()
upload_parser.add_argument('image_file', location='files', type='file', required=True)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@api.route('/', methods=["GET" , "POST"])
class Upload_controller(Resource):

    @api.doc('Create image bit string entity.')
    @api.expect(upload_parser)
    def post(self):
        image_file = request.files['image_file']
        if not allowed_file(image_file.filename):
            return {'message': 'Only JPEG or PNG files are allowed.'}, 400
        
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        return Image_service.Create_image_bit_string(image_base64)
    
    @api.doc('Get image  bit strings.')
    @api.marshal_list_with(upload_dto, envelope='data')
    def get(self):
        return Image_service.get_image_bit_strings()

@api.route('/<int:id>', methods=["GET"])
class Upload_id_controller(Resource):

    @api.doc('Get image bit string by id.')
    @api.marshal_list_with(upload_dto, envelope='data')
    def get(self, id: int):
        return Image_service.get_image_bit_string(id)

