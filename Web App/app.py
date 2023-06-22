from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_key = request.form['customer_key']
        branch = request.form['branch']
        tag = request.form['tag']
        product = request.form['product']
        hand_side = request.form['hand_side']
        reinstall = request.form.get('reinstall') is not None
        ethercat_right_arm = request.form['ethercat_right_arm']
        arm_ip_right = request.form['arm_ip_right']
        ethercat_left_arm = request.form['ethercat_left_arm']
        arm_ip_left = request.form['arm_ip_left']
        ur_robot_type = request.form['ur_robot_type']

        oneliner = "bash <(curl -Ls bit.ly/run-aurora) server_and_nuc_deploy --branch " + branch + " customer_key=\"" + customer_key + "\" product=" + product + " reinstall=" + str(reinstall)

        if product == "arm_hand_e":
            oneliner += " hand_side=" + hand_side

        if hand_side == "left":
            oneliner += " ethercat_left_arm=\"" + ethercat_left_arm + "\""
            oneliner += " arm_ip_left=\"" + arm_ip_left + "\""
        elif hand_side == "right":
            oneliner += " ethercat_right_arm=\"" + ethercat_right_arm + "\""
            oneliner += " arm_ip_right=\"" + arm_ip_right + "\""
        else:
            oneliner += " ethercat_right_arm=\"" + ethercat_right_arm + "\""
            oneliner += " arm_ip_right=\"" + arm_ip_right + "\""
            oneliner += " ethercat_left_arm=\"" + ethercat_left_arm + "\""
            oneliner += " arm_ip_left=\"" + arm_ip_left + "\""

        return render_template('index.html', oneliner=oneliner)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
