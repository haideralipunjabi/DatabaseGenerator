import src.webManager
import src.dbgenerator

print("Database Generator - Hack-e-Sta")
if(src.webManager.Connection().isserveravailable()):
    generator = src.dbgenerator.DatabaseGenerator()