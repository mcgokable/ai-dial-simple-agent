from typing import Any

from task.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "search_users"

    @property
    def description(self) -> str:
        return "Search users in the user service"

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - name: str
        # - surname: str
        # - email: str
        # - gender: str
        # None of them are required (see UserClient.search_users method)
        return {"type": "object", "properties": {"name": {"type": "string"}, "surname": {"type": "string"}, "email": {"pe": "string"}, "gender": {"type": "string"}}, "required": []}

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        try:
            # 1. Call user_client search_users (with `**arguments`) and return its results
            result = self._user_client.search_users(**arguments)
            return result
            # 2. Optional: You can wrap it with `try-except` and return error as string `f"Error while searching users: {str(e)}"`
        except Exception as e:
            return f"Error while searching users: {str(e)}"
