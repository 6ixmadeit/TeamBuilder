import uuid

def generate_code():
        code = str(uuid.uuid4()).replace("-", "")[:6] # Takes a UUID4 string and turns it into a 6 digit string
        return code