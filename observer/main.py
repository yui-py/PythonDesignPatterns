from observer.listeners import EmailListener
from observer.listeners import LoggingListener
from observer.analyzers.analyzer import Analyzer


def main():
    analyzer = Analyzer()
    analyzer.events.subscribe("test", EmailListener())
    analyzer.events.subscribe("test", LoggingListener())
    analyzer.do_something()


if __name__ == "__main__":
    main()
