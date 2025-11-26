from time import sleep


def pack_products(product_list):
    """
    Moves products to drop-off location.
    [Team Function] - Coordinates with mechanical end effector system.

    Args:
        product_list (list): 2D list of products [[name, price], ...]

    Returns:
        None - Outputs Q-Arm motor commands
    """
    if len(product_list) == 0:
        print("No products to pack")
        return

    for product in product_list:
        current = product[0].lower()
        print(f"Packing {product[0]}")

        # Sponge
        if 'Sponge' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-35)
            arm.rotate_base(19)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(47)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-50)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        # Bottle
        elif 'Bottle' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-20)
            arm.rotate_base(11)
            arm.rotate_elbow(-11)
            arm.rotate_shoulder(46)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-46)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        # Rook
        elif 'Rook' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-35)
            arm.rotate_base(5)
            arm.rotate_elbow(-8)
            arm.rotate_shoulder(46)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-46)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        # D12
        elif 'D12' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-30)
            arm.rotate_base(-4.6)
            arm.rotate_elbow(-7)
            arm.rotate_shoulder(47)
            arm.rotate_gripper(70)
            arm.rotate_shoulder(-45)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        # Witchhat
        elif 'Witchhat' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-25)
            arm.rotate_base(0)
            arm.rotate_elbow(-10)
            arm.rotate_shoulder(45)
            arm.rotate_gripper(75)
            arm.rotate_shoulder(-43)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        # Bowl
        elif 'Bowl' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-30)
            arm.rotate_base(-11)
            arm.rotate_elbow(-5)
            arm.rotate_shoulder(49)
            arm.rotate_gripper(70)
            arm.rotate_shoulder(45)

            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)
            arm.home()

        else:
            print(f"No packing sequence for {product[0]}")

    arm.end_arm_connection()
    print("All products packed successfully")

