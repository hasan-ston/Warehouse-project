from time import sleep

try:
    from Common.qarm_interface_wrapper import *
except ImportError:
    QuanserInteractiveLabs_2DOF = None


def pack_products(product_list):

    if QuanserInteractiveLabs_2DOF:
        arm = QuanserInteractiveLabs_2DOF()
        arm.start_arm_connection()
    else:
        arm = None
        print("Q-Arm hardware not available - running in simulation mode")

    for item in product_list:
        product_name = item[0]
        current = product_name.strip().lower()

        print(f"Packing {current}...")

        if 'sponge' in current:
            if arm:
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
            else:
                print("  [Simulation] Executing Sponge packing sequence")

        elif 'bottle' in current:
            if arm:
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
            else:
                print("  [Simulation] Executing Bottle packing sequence")

        elif 'rook' in current:
            if arm:
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
            else:
                print("  [Simulation] Executing Rook packing sequence")

        elif 'd12' in current:
            if arm:
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
            else:
                print("  [Simulation] Executing D12 packing sequence")

        elif 'bowl' in current:
            if arm:
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
            else:
                print("  [Simulation] Executing Bowl packing sequence")

        elif 'witch' in current or 'hat' in current:
            if arm:
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
                print("  [Simulation] Executing WitchHat packing sequence")

        else:
            print(f"Warning: No packing sequence defined for '{product_name}'")
            continue

        print(f"{product_name} packed successfully")

    if arm:
        arm.end_arm_connection()

    print("\nAll products packed successfully")
