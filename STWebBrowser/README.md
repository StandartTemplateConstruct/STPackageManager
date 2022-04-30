# ST Web Browser
A keyboard controlled multitab browser that overlays OpenMMLab model processing result on the web pages open in it

# Platform 

 - SwiftUI
 - Unity

# Models

 - https://github.com/open-mmlab/mmediting
 - https://github.com/open-mmlab/mmflow
 - https://github.com/open-mmlab/mmdetection3d
 - https://github.com/open-mmlab/mmocr
 - https://github.com/open-mmlab/mmaction2
 - https://github.com/open-mmlab/mmrotate



# multi device browser

Got builtin HTTP server/React native web interface for control of navigation, tab switching, audio selection

Receives keyboard/mouse input via web socket interface

A hot key for sending a tab to another device


# ROS node 

Has built in ROS node: camera, gps movement, actuators and camera for browser navigation 
## iOS app

 - SwiftUI interface
 - CoreML models - exported by MMDeploy to ONNX Runtime
 - On device labeling generates a request to upload a screenshot of page to the learning service server

# new reqs 

 - streams out tabs as rtmp
 - able to show the overlayed labels from remote server

# old stuff 

## UI

### Tab views

 - *hotkey*: `1`..`9`,`0`

 - Shows a webpage
 - Has address bar
   - If search term is entered, google search is performed
 - button to enter **Labeling view**
 - any object that is labeled by user and recognized is highlighted. It can be interacted with **Labeled object popup**

#### Labeling view
 
 - Allows to label an underlying webpage in a modal overlay
    - Boxes
    - Automatic segmentation
    - Semantic autolabeling
      -   People
      -   Vehicles
      -   Hands
      -   People skeletons
      -   Objects recognizable by image nets
      -   UI elements


#### Labeled object

 - *checkbox* Show object on composite view
 - *textfield* Fully qualified a **Semantic Path** label for the object

### Composite view

 - *hotkey*: `~`
 
Shows all objects, whose fully qualified Semantic


# Semantic Label

## Semantic Label Context

 - url
   - url features 
 - title
   - title features
 - webpage features

## Semantic Label Class Tree

 - UI
   - Video Player
   - Button
   - Text Field
   - Text
 - Real World Object
   - Humanoid
     - Human
     - Bot   
   - Vehicle
     - Truck
     - Tank
     - Car
     - Train
     - Boat
     - Airplane
   - Item
   - Landscape
   - Building

#AR view 

## HumanROS component

## on screen keyboard for recognized connected screens without touchscreen 

# Architecture

SwiftUI app that streams the contents of its WebViews to the Python server over RTMP

Python server runs several models on the video, serves results to the subscribers over MixtreamProtocol

## MixtreamProtocol

# Datasets

 - https://paperswithcode.com/dataset/howto100m
 - https://github.com/open-mmlab/mmaction2

