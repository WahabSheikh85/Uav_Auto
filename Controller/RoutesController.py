from UAVAUTO_VERSION_4.Model.Routes import Routes
from UAVAUTO_VERSION_4.config import db

class RoutesController():

    @staticmethod
    def insert_route(data):
        route = Routes(admin_id=data['admin_id'],name=data['name'])
        db.session.add(route)
        db.session.commit()
        return {'id':route.id,'admin_id':route.admin_id,'name':route.name}

    @staticmethod
    def get_routes():
        routes = Routes.query.filter_by(validity=1).all()
        if routes:
            return [{'id':r.id,'admin_id':r.admin_id,'name':r.name} for r in routes]

        return {}