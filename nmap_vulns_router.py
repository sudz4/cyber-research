from scapy.all import conf, Route

def get_default_gateway():
    # get default route
    default_route = [route for route in conf.route.routes if route[2] == "0.0.0.0"]

    if not default_route:
        return None

    default_route = default_route[0]

    # get default gateway (router)
    default_gateway = default_route[2]

    return default_gateway

if __name__ == "__main__":
    default_gateway = get_default_gateway()
    if default_gateway:
        print(f"Default gateway (router) IP address is: {default_gateway}")
    else:
        print("No default gateway found.")
