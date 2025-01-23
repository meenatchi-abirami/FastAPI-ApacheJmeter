from dataforge.src.common_modules.database import DatabaseManager

database_manager = DatabaseManager.get_instance()
engine = database_manager.engine
SessionLocal = database_manager.session_local
metadata = database_manager.metadata
get_db = database_manager.get_db