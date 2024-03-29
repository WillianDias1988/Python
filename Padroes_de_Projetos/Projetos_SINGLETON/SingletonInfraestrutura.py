class HealthCheck:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(
                HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self) -> None:
        self._servers = []

    def addServers(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Servers 5")


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServers()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers(2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])
