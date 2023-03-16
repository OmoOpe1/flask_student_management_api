from flask_restx import Namespace, Resource


order_namespace=Namespace('orders', description="Namespace for orders")


@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self):
        """
            Get all orders
        """
        pass

    def post(self):
        """
            Place a new order.
        """
        pass

@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self, order_id):
        """
            Retrieve an order by id.
        """
        pass

    def put(self, order_id):
        """
            Update an order with id.
        """
        pass

    def delete(self, order_id):
        """
            Delete an order with id.
        """
        pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUserId(Resource):

    def get(self, user_id, order_id):
        """
            Retrieve a users specific order.
        """
        pass

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):

    def get(self, order_id):
        """
            Get all orders for specific user.
        """
        pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    def patch(self, order_id):
        """
            Update an orders status.
        """
        pass