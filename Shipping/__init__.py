import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 80
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds

# client = EurekaClient(
#             eureka_server="http://103.13.231.22:8761/eureka/", 
#             app_name="Shipping_Service", 
#             instance_port=your_rest_server_port)
# client.start()
# result = client.do_service("APP_NAME", "/context/path", return_type="json")
eureka_client.init(eureka_server="http://103.13.231.22:8761/eureka",
                   app_name="Shipping-Service",
                   instance_port=your_rest_server_port)
