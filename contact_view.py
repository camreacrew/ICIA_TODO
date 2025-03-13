from flask import Blueprint, render_template, request, redirect, Blueprint
contact_app = Blueprint('contact_app', __name__, url_prefix='/contact')

contacts = []
cno = 1

@contact_app.route('/list')
def list():
    return render_template('contact/list.html', contacts = contacts)

@contact_app.route('/write', methods = ['post'])
def add():
    global cno
    cname = request.form.get('cname', None)
    contact_num = request.form.get('contact_num', None)
    address = request.form.get('address', None)
    new_contact = {'cno':cno, 'cname':cname, 'contact_num':contact_num, 'address':address}
    contacts.append(new_contact)
    cno += 1
    return redirect('/contact/list')


@contact_app.route('/delete', methods = ['post'])
def delete():
    cno = int(request.form.get('cno'))
    for contact in contacts:
        if contact['cno'] == cno:
            contacts.remove(contact)
    return redirect('/contact/list')