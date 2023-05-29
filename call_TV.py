from HW import TV

def main(): 

    television = TV()
    television.turnOn()
    television.setChannel(50)
    chnnael_verson = television.getChannel()
    television.setVolume(10)
    channel_voice = television.getVolumeLevel()
    print(chnnael_verson, channel_voice)

main()