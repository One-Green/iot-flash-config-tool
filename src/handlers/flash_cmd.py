import platform


class FlashCmd:
    def __init__(self):
        pass

    @staticmethod
    def __envs_for_windows(env):
        return f"set {env}"

    def __base_cmd_generator(self, src_path, **kwargs):
        envs = []
        for k, v in kwargs.items():
            envs.append(f"{k}={v}")
        # if windows add 'set' suffix eg "set WIFI_PASSWORD=my-wifi-password"
        if platform.system() == "Windows":
            envs = list(map(self.__envs_for_windows, envs))
        envs = " ".join(envs)
        cmd = f"cd {src_path} && pio update && {envs} pio run -t upload"
        return cmd

    def get_main_microchip_cmd(
        self,
        src_path: str,
        wifi_ssid: str,
        wifi_password: str,
        api_gateway_url: str,
        api_gateway_basic_auth_user: str,
        api_gateway_basic_auth_password: str,
        node_tag: str,
        mqtt_server: str,
        mqtt_port: str,
        mqtt_user: str,
        mqtt_password: str,
    ):
        return self.__base_cmd_generator(
            src_path=src_path,
            WIFI_SSID=wifi_ssid,
            WIFI_PASSWORD=wifi_password,
            API_GATEWAY_URL=api_gateway_url,
            API_GATEWAY_BASIC_AUTH_USER=api_gateway_basic_auth_user,
            API_GATEWAY_BASIC_AUTH_PASSWORD=api_gateway_basic_auth_password,
            NODE_TAG=node_tag,
            CHECK_NODE_TAG_DUPLICATE="false",  # decommissioned
            MQTT_SERVER=mqtt_server,
            MQTT_PORT=mqtt_port,
            MQTT_USER=mqtt_user,
            MQTT_PASSWORD=mqtt_password,
        )
