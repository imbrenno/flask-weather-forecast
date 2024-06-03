from flask import jsonify, request, Blueprint, make_response
from main.database.models.user_model import Users

bp = Blueprint(
    "user",
    __name__,
    template_folder="templates",
    url_prefix="/user",
)


class UsersCtrl:

    @staticmethod
    @bp.route("/create", methods=["POST"])
    def create_user():
        try:
            data = request.get_json()
            user = Users.get_one(data["username"])
            if user:
                return make_response(
                    jsonify(
                        {"message": "User conflict"},
                    ),
                    409,
                )

            new_user = Users(
                data["username"],
                data["email"],
            )
            new_user.save()
            return make_response(
                jsonify(
                    {"message": "User added successfully"},
                ),
                200,
            )

        except Exception as e:
            print(f"Error in Users 'create_user Exception: {e}")

    @staticmethod
    @bp.route("/list", methods=["GET"])
    def get_users():
        try:
            users = Users.get_all()
            user_list = [
                {
                    "username": user["username"],
                    "email": user["email"],
                }
                for user in users
            ]
            return make_response(jsonify({"users": user_list}), 200)
        except Exception as e:
            print(f"Error in Users 'list' Exception: {e}")

    @staticmethod
    @bp.route("/retrieve/<username>", methods=["GET"])
    def get_user_by_username(username):
        try:
            user = Users.get_one(username)
            if user:
                return make_response(
                    jsonify(
                        {
                            "username": user["username"],
                            "email": user["email"],
                        }
                    )
                )
            else:
                return make_response(jsonify({"message": "User not found"})), 404

        except Exception as e:
            print(f"Error in Users 'get_user' Exception: {e}")

    @staticmethod
    @bp.route("/delete/<username>", methods=["DELETE"])
    def delete_user_by_username(username):
        try:
            user = Users.get_one(username)
            if user:
                Users.delete(username)
                return jsonify(
                    [
                        {"message": "User delected successfully"},
                        {
                            "username": user["username"],
                            "email": user["email"],
                        },
                    ]
                )

            return jsonify({"message": "User not found"}), 404

        except Exception as e:
            print(f"Error in Users 'delete' Exception: {e}")

    @staticmethod
    @bp.route("/update/<username>", methods=["PUT"])
    def update_user_by_username(username):
        try:
            data = request.get_json()
            user = Users.get_one(username)
            if user:
                Users.update(username, data)
                return jsonify(
                    [
                        {"message": "User update successfully"},
                        data,
                    ]
                )

            return jsonify({"message": "User not found"}), 404

        except Exception as e:
            print(f"Error in Users 'update_user' Exception: {e}")
