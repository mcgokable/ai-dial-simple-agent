from typing import Any

from task.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "get_user_by_id"

    @property
    def description(self) -> str:
        return "Get a user by id from the user service"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        return {"type": "object", "properties": {"id": {"type": "number"}}, "required": ["id"]}

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            # 1. Get int `id` from arguments
            user_id = arguments.get("id", None)
            if not user_id:
                return "User id is required"
            # 2. Call user_client get_user and return its results
            result = self._user_client.get_user(user_id)
            # 3. Optional: You can wrap it with `try-except` and return error as string `f"Error while retrieving user by id: {str(e)}"`
            return result
        except Exception as e:
            return f"Error while retrieving user by id: {str(e)}"