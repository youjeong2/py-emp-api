import com_py_api.home.api import home
import com_py_emp_api.item.api import Item, Items
import com_py_emp_api.cheese.api import Cheese, Dairy

def initialize_routes(api):
    print('===2===')
    api.add_resource(Home, '/api')
    api.add_resource=(Item, '/api/item/<string:id>')
    api.add_resource=(Items, '/api/items')
    api.add_resource=(Cheese, '/api/cheese/<string:id>')
    adpi.add_resource=(Dairy, '/api/Dairy/')