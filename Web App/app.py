import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)

def get_release_versions():
    url = "https://api.github.com/repos/shadow-robot/aurora/releases"
    response = requests.get(url)
    if response.status_code == 200:
        releases = response.json()
        versions = [release["tag_name"] for release in releases]
        return versions
    return []

def get_branches():
    url = "https://api.github.com/repos/shadow-robot/aurora/branches"
    response = requests.get(url)
    if response.status_code == 200:
        branches = response.json()
        branch_names = [branch["name"] for branch in branches]
        return branch_names
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_key = request.form['customer_key']
        playbook = request.form['playbook']
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

        oneliner = "bash <(curl -Ls https://raw.githubusercontent.com/shadow-robot/aurora/"+tag+"/bin/run-ansible.sh) " + playbook + " --branch " + branch + " customer_key=\"" + customer_key + "\" product=" + product + " reinstall=" + str(reinstall)

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

        return render_template('index.html', oneliner=oneliner, versions=get_release_versions(), branches=get_branches())

    return render_template('index.html', versions=get_release_versions(), branches=get_branches())

if __name__ == '__main__':
    app.run()
