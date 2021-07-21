looking_for_marker = False
pid_x = PIDCtrl()
pid_y = PIDCtrl()
pid_Pitch = PIDCtrl()
pid_Yaw = PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_MarkerList = RmList()


def fire_gun():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    led_ctrl.gun_led_on()
    ir_blaster_ctrl.fire_once()
    time.sleep(2)
    ir_blaster_ctrl.stop()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.recenter()
    pass


def vision_recognized_marker_number_one(msg):
    global looking_for_marker
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    global pid_team4
    global looking_for_marker
    global room_id
    global vision_one_detection_type

    if looking_for_marker:
        print("Detected marker 1")
        looking_for_marker = False
        if vision_one_detection_type == "none":  # Skip the function call if for some reason the type is empty
            pass
        else:
            # Check which room we are at
            if room_id == 'a':
                if vision_one_detection_type == "at_the_door":
                    # Move into room with A-dimensions, and center in front of marker to fire
                    vision_one_detection_type = "in_the_room"  # Update to tell the program we are in the room
                    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
                    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    gimbal_ctrl.recenter(0)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 4.26)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2)
                    # Enable marker detection and center gimbal, then fire.
                    looking_for_marker = True
                    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
                    # Add the loop again
                elif vision_one_detection_type == "in_the_room":
                    gimbal_ctrl.recenter(0)
                    gimbal_ctrl.pitch_ctrl(0)
                    fire_gun()
                    # Move out of room A
                    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
                    gimbal_ctrl.recenter(0)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 4.26)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)


            elif room_id == 'b':
                if vision_one_detection_type == "at_the_door":
                    # Move into room with B-dimensions.
                    vision_one_detection_type = "in_the_room"
                    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    gimbal_ctrl.recenter()
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.73)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.25)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 1.45)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 1)
                    robot_ctrl.set_mode(rm_define.robot_mode_free)
                    gimbal_ctrl.recenter()
                    # Enable marker detection and center gimbal, then fire.
                    looking_for_marker = True
                    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

                elif vision_one_detection_type == "in_the_room":
                    gimbal_ctrl.pitch_ctrl(0)
                    fire_gun()
                    # Move out of room B
                    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
                    gimbal_ctrl.recenter()
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 1)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 1.45)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.45)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.73)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 92)

            elif room_id == 'c':
                if vision_one_detection_type == "at_the_door":
                    # Move into room with C-dimensions.
                    vision_one_detection_type = "in_the_room"
                    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    gimbal_ctrl.recenter()
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 4.7)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.29)
                    robot_ctrl.set_mode(rm_define.robot_mode_free)
                    gimbal_ctrl.recenter()
                    # Enable marker detection and center gimbal, then fire.
                    looking_for_marker = True
                    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

                elif vision_one_detection_type == "in_the_room":
                    gimbal_ctrl.pitch_ctrl(0)
                    fire_gun()
                    # Move out of room C
                    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
                    gimbal_ctrl.recenter()
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 2.3)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 4.7)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 91)

            # Room id must be 'd' otherwise, so an else here is ok.
            else:
                if vision_one_detection_type == "at_the_door":
                    # Move into room with D-dimensions.
                    vision_one_detection_type = "in_the_room"
                    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    gimbal_ctrl.recenter()
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 5)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    robot_ctrl.set_mode(rm_define.robot_mode_free)
                    gimbal_ctrl.recenter()
                    # Enable marker detection and center gimbal, then fire.
                    looking_for_marker = True
                    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

                elif vision_one_detection_type == "in_the_room":
                    gimbal_ctrl.pitch_ctrl(0)
                    fire_gun()
                    # Move out of room D
                    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
                    gimbal_ctrl.recenter(0)
                    chassis_ctrl.set_trans_speed(.5)
                    chassis_ctrl.move_with_distance(0, 4.7)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 87)
                    gimbal_ctrl.recenter()


def vision_recognized_marker_number_two(msg):
    global looking_for_marker
    global room_id

    if looking_for_marker:
        print("Detected marker 2")
        looking_for_marker = False
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.recenter()
        if room_id == "d":
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            time.sleep(1)
            gimbal_ctrl.recenter()
            print("Successful 180..")


def vision_recognized_marker_number_three(msg):
    global looking_for_marker
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    global pid_team4
    global room_id
    global at_start

    if looking_for_marker:
        print("Detected marker 3")
        looking_for_marker = False
        # These will look to detect a person.
        # Check which room we are at
        if room_id == 'a':
            # Move into room with A-dimensions.
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.recenter()
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.26)
            gimbal_ctrl.pitch_ctrl(35)
            vision_ctrl.enable_detection(rm_define.vision_detection_people)

            # Make moves to position to detect person / aim gimbal
            def vision_recognized_people(msg):
                print("there you are")
                # Move out of room A

            vision_ctrl.disable_detection(rm_define.vision_detection_people)
            gimbal_ctrl.pitch_ctrl(0)
            gimbal_ctrl.recenter()
            media_ctrl.play_sound(rm_define.media_custom_audio_0)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.26)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            # Lead person to start
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            time.sleep(4)
            'End sitting on start line'
            # Return to front of room A
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.3)


        elif room_id == 'b':
            # Move into room with B-dimensions.

            robot_ctrl.set_mode(rm_define.robot_mode_free)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.recenter()
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.73)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.25)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 1.45)
            gimbal_ctrl.pitch_ctrl(35)
            vision_ctrl.enable_detection(rm_define.vision_detection_people)

            # Make moves to position to detect person / aim gimbal
            def vision_recognized_people(msg):
                print("there you are")

            # Move out of room B
            vision_ctrl.disable_detection(rm_define.vision_detection_people)
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            gimbal_ctrl.pitch_ctrl(0)
            gimbal_ctrl.recenter()
            media_ctrl.play_sound(rm_define.media_custom_audio_0)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 1.45)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.25)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.73)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise,
                                            90)  # Orientate chassis to move back through hall to start
            # Lead person to start
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.9)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(45, 3.1)
            time.sleep(1)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            time.sleep(4)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.1)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.7)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            time.sleep(4)
            # Return to front of room B
            'Rotate 180 here'
            'Add the travel needed to get back to A, then travel back to B below'
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.3)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.1)
            chassis_ctrl.move_with_distance(-45, 3.1)
            time.sleep(1)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            time.sleep(4)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.9)
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            gimbal_ctrl.recenter()

        elif room_id == 'c':
            # Move into room with C-dimensions.
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.recenter()
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.7)
            gimbal_ctrl.pitch_ctrl(35)
            vision_ctrl.enable_detection(rm_define.vision_detection_people)

            # Make moves to position to detect person / aim gimbal
            def vision_recognized_people(msg):
                print("there you are")

            # Move out of Room C
            vision_ctrl.disable_detection(rm_define.vision_detection_people)
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            gimbal_ctrl.pitch_ctrl(0)
            media_ctrl.play_sound(rm_define.media_custom_audio_0)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.4)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            # Lead person to start
            'Code here...'
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 3.8)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.9)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(45, 3.1)
            time.sleep(1)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            time.sleep(4)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.1)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            time.sleep(4)
            # Return to front of room C
            'Rotate 180 here'
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.3)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.1)
            chassis_ctrl.move_with_distance(-45, 3.1)
            time.sleep(1)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 92)
            time.sleep(4)
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.9)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 3.9)
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            gimbal_ctrl.recenter()


        # Room id must be 'd' otherwise, so an else here is ok.
        else:
            # Move into room with D-dimensions.
            robot_ctrl.set_mode(rm_define.robot_mode_free)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.recenter()
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.7)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.9)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.pitch_ctrl(35)
            vision_ctrl.enable_detection(rm_define.vision_detection_people)

            # Make moves to position to detect person / aim gimbal
            def vision_recognized_people(msg):
                print("there you are")

            # Move out of Room D
            vision_ctrl.disable_detection(rm_define.vision_detection_people)
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            gimbal_ctrl.pitch_ctrl(0)
            media_ctrl.play_sound(rm_define.media_custom_audio_0)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.9)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.7)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

            # Lead person to start
            at_start = True  # Robot will be at the start after the code
            gimbal_ctrl.recenter()
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 0.3)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 3.9)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 4.9)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(45, 3.1)
            time.sleep(1)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            time.sleep(1)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.1)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.set_trans_speed(.5)
            chassis_ctrl.move_with_distance(0, 2.3)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            # We are coming from the last room, so no need to return. End after this.


def start():
    global looking_for_marker
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    global pid_team4
    global room_id
    global vision_one_detection_type
    global at_start

    print("starting...")
    at_start = False
    media_ctrl.record(1)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Move to outside room A
    room_id = 'a'
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 2.3)
    # Rotate gimbal to look for marker
    vision_one_detection_type = "at_the_door"
    gimbal_ctrl.yaw_ctrl(-45)

    looking_for_marker = True
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(1.5)
    while looking_for_marker == True:
        print("starting loop")
        pass

    # Continue moving on to room "B"
    gimbal_ctrl.recenter()
    time.sleep(1)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print(looking_for_marker)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    room_id = 'b'
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 2.1)
    chassis_ctrl.move_with_distance(-45, 3.1)
    time.sleep(1)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 92)
    time.sleep(4)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 4.9)
    gimbal_ctrl.recenter()
    vision_one_detection_type = "at_the_door"
    gimbal_ctrl.yaw_ctrl(-45)
    time.sleep(2)

    looking_for_marker = True
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    while looking_for_marker == True:
        print("starting second loop")
        pass

    # Continue moving on to room "C"

    time.sleep(1)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print(looking_for_marker)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.recenter()
    room_id = 'c'
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 3.9)
    vision_one_detection_type = "at_the_door"
    gimbal_ctrl.yaw_ctrl(-45)
    time.sleep(2)
    looking_for_marker = True
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    while looking_for_marker == True:
        print("starting third loop")
        pass

    # Continue moving on to room "D"
    gimbal_ctrl.recenter()
    time.sleep(1)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print(looking_for_marker)
    room_id = 'd'
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.5)
    chassis_ctrl.move_with_distance(0, 0.3)
    vision_one_detection_type = "at_the_door"
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.yaw_ctrl(-45)
    time.sleep(2)
    looking_for_marker = True
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    while looking_for_marker == True:
        print("starting fourth loop")
        pass
    if not at_start:
        # go to start
        # otherwise it will end
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 0.3)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 4.2)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 4.9)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(45, 3.1)
        time.sleep(1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        time.sleep(1)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 2.1)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 2.3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        pass
    print("ending...")
    media_ctrl.record(0)
