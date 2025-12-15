from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "update_user"

    @property
    def description(self) -> str:
        return "Update a user in the user service"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema:
        # - id: number, required, User ID that should be updated.
        # - new_info: UserUpdate.model_json_schema()

        user_update_schema = UserUpdate.model_json_schema()
        schema = {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID that should be updated.",
                },
                "new_info": {
                    "type": "object",
                    "description": "New user information to update",
                    "properties": user_update_schema.get("properties", {}),
                },
            },
            "required": ["id"],
        }
        
        # Include $defs at the top level if they exist (for nested models like Address, CreditCard)
        if "$defs" in user_update_schema:
            schema["$defs"] = user_update_schema["$defs"]
            
        return schema

    def execute(self, arguments: dict[str, Any]) -> str:
        # 1. Get user `id` from `arguments`
        try:
            user_id = arguments["id"]
            # 2. Get `new_info` from `arguments` and create `UserUpdate` via pydentic `UserUpdate.model_validate`
            new_info = arguments.get("new_info", None)
            if not new_info:
                return "New info is required"
            user_update = UserUpdate.model_validate(new_info)
            # 3. Call user_client update_user and return its results
            return self._user_client.update_user(user_id, user_update)
        # 4. Optional: You can wrap it with `try-except` and return error as string `f"Error while creating a new user: {str(e)}"`
        except Exception as e:
            return f"Error while updating user: {str(e)}"
