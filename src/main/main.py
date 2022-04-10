import Controller.LoadData as loadData
import Controller.userInteraction as uia

def main() -> None:
    #Entry point of the application
    loadData.loadData()
    print("The database is ready!")
    uia.userLoop()

if __name__ == '__main__':
    main()
