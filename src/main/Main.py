import Controller.InitData as loadData
import Controller.UserInteraction as uia


def main() -> None:
    # Entry point of the application
    loadData.loadData()
    print("The database is ready!")
    uia.userLoop()


if __name__ == '__main__':
    main()
