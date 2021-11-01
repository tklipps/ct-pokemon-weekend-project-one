from flask import render_template, request, redirect, url_for, flash
import requests
from .forms import PokeForm
from flask_login import login_required
from .import bp as main

@main.route('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/pokeinfo', methods=['GET', 'POST'])
@login_required
def pokeinfo():
    form = PokeForm()
    if request.method == 'POST' and form.validate_on_submit():
        poke = request.form.get('poke_id')
        url = f"https://pokeapi.co/api/v2/pokemon/{poke}"
        
        response = requests.get(url)
        if response.ok:            
            data = response.json()
                  
            
            poke_dict={
                'poke_name':data['name'],
                'base_hp':data['stats'][0]['base_stat'],
                'base_defense':data['stats'][2]['base_stat'],
                'base_attack':data['stats'][1]['base_stat'],                    
                'front_shiny':data["sprites"]["front_shiny"],
            }
                
            print(poke_dict)
            return render_template('pokeinfo.html.j2', poke=poke_dict, form=form)     
        
        else:
            return "That's not a Pokemon!!!"
            

    return render_template('pokeinfo.html.j2', form=form)