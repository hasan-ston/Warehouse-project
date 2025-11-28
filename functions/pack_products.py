from time import sleep
from library.quanser import QuanserInteractiveLabs_2DOF


def pack_products(product_list):
    arm = QuanserInteractiveLabs_2DOF()
    arm.start_arm_connection()

    for product in product_list:
        product_name = product[0]
        current = product_name.strip().lower()

        print(f"\nPacking {current}...")

        # Check which product and execute sequence
        if 'sponge' in current:
            if arm:
                arm.rotate_gripper(180)
                arm.rotate_gripper(-35)

                arm.rotate_base(19)
                arm.rotate_elbow(-12)
                arm.rotate_shoulder(47)
                arm.rotate_gripper(80)
                arm.rotate_shoulder(-50)

                # Parcel drop
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
                print(" Executing Sponge packing sequence") # for testing; REMOVE THIS

        elif 'bottle' in current:
            if arm:
                arm.rotate_gripper(180)
                arm.rotate_gripper(-20)

                arm.rotate_base(11)
                arm.rotate_elbow(-11)
                arm.rotate_shoulder(46)
                arm.rotate_gripper(80)
                arm.rotate_shoulder(-46)

                # Parcel drop
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
                print("Executing Bottle packing sequence") # Remove this

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
                print("Executing Rook packing sequence")

        elif 'd12' in current:
            if arm:
                arm.rotate_gripper(180)
                arm.rotate_gripper(-30)

                arm.rotate_base(-4.6)
                arm.rotate_elbow(-7)
                arm.rotate_shoulder(47)
                arm.rotate_gripper(70)
                arm.rotate_shoulder(-45)

                # Parcel drop
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
                print("Executing D12 packing sequence")

        elif 'witch' in current:
            if arm:
                arm.rotate_gripper(180)
                arm.rotate_gripper(-25)

                arm.rotate_base(0)
                arm.rotate_elbow(-10)
                arm.rotate_shoulder(45)
                arm.rotate_gripper(75)
                arm.rotate_shoulder(-43)

                # Parcel drop
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
                print("Executing Bowl packing sequence")

        elif 'bowl' in current:
            if arm:
                arm.rotate_gripper(180)
                arm.rotate_gripper(-35)

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
                print("Executing WitchHat packing sequence")

        else:
            print(f"Warning: No packing sequence defined for '{product_name}'")
            continue

        print(f"{product_name} packed successfully")

    if arm:
        arm.end_arm_connection()

    print("\nAll products packed successfully")