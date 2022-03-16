import QtQuick 2.0

Item {
    property string title
    property color buttonColor
    property int buttonState: 0

    Rectangle{
        anchors.fill: parent
        color: buttonColor
        radius: 5
        Text {
            id: buttonText
            text: title
            color: "white"
            anchors.centerIn: parent
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                if(buttonState == 0){
                    console.log("Start")
                    buttonState = 1
                    buttonText.text = "Stop"
                }else{
                    console.log("Stop")
                    buttonState = 0
                    buttonText.text = title
                }
            }
        }
    }
}
