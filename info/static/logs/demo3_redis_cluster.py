from rediscluster import StrictRedisCluster


def demo():
    startup_nodes = [
        {"host": "172.16.28.143", "port": 7000},
        {"host": "172.16.28.143", "port": 7001},
        {"host": "172.16.28.143", "port": 7002}
    ]
    src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    try:
        result = src.set('name', 'laowang')
        print(result)
        value = src.get('name')
        print(value)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    demo()
