<template>
	<div id="container">

		<div id="erreur-container">
			<div v-if="champs_non_remplis" id="erreur-champs">
				<p>Remplissez bien tout les champs</p>
			</div>

			<div v-if="erreur_bons_mauvais" id="erreur-bons-mauvais">
				<p>La somme des bons et des mauvais ne peut être différent du total</p>
			</div>
		</div>

		<div id="post-tri-container">
			<div class="tri-input-div">
				<label for="of-input" class="tri-label">OF</label>
				<input id="of-input" type="text" class="tri-input" v-model="of">
			</div>
			<div class="tri-input-div">
				<label for="symbol-input" class="tri-label">Symbole</label>
				<input id="symbol-input" type="text" class="tri-input" v-model="symbole">
			</div>
			<div class="tri-input-div">	
				<label for="client-input" class="tri-label">Client</label>
				<input id="client-input" type="text" class="tri-input" v-model="client">
			</div>
			<div class="tri-input-div">	
				<label for="defaut-input" class="tri-label">Defaut</label>
				<input id="defaut-input" type="text" class="tri-input" v-model="defaut">
			</div>
			<div class="tri-input-div">	
				<label for="a-trier-input" class="tri-label">A trier</label>
				<input id="a-trier-input" type="number" class="tri-input" v-model="a_trier">
			</div>	
			<div class="tri-input-div">
				<label for="bonnes-input" class="tri-label">Bonnes</label>
				<input id="bonnes-input" type="number" class="tri-input" v-model="bonnes">
			</div>
			<div class="tri-input-div">	
				<label for="mauvais-input" class="tri-label">Mauvais</label>
				<input id="mauvais-input" type="number" class="tri-input" v-model="mauvaises">
			</div>
			<div class="tri-input-div">
				<label for="est-trie-input" class="tri-label">Est Trié</label>
				<input id="est-trie-input" type="checkbox" class="tri-input" v-model="est_trie" style="width: auto;">
			</div> 
			<button @click="postTri">Post</button> 
		</div>

	</div>

	
</template>

<script>
import { ref, reactive, onMounted, computed } from	'vue';
import axios from 'axios'

export default {
	name: 'Tri',
	components: {
	},
	setup()
	{

		let data = reactive({}) 


		let of		  = ref("");
		let symbole	  = ref("");
		let client	  = ref("");
		let defaut    = ref("");
		let a_trier	  = ref(0);
		let bonnes	  = ref(0);
		let mauvaises = ref(0);
		let est_trie  = ref(false);

		let champs_non_remplis = ref(false);
		let erreur_bons_mauvais = ref(false);

		let bool_erreur_champ = computed(()=>{
			return (of.value=="" || symbole.value=="" || client.value=="" || defaut.value=="" || a_trier.value<=0);
		})

		let bool_erreur_tri = computed(()=>{
			let a = parseInt(bonnes.value)
			let b = parseInt(mauvaises.value)
			let c = parseInt(a_trier.value)

			return a+b != c
		})


		let postTri = ()=>{
			if (bool_erreur_champ.value){ //si les champs ne sont pas remplis 
				champs_non_remplis.value = true;
			}
			else { champs_non_remplis.value = false; } 
			if (bool_erreur_tri.value) // si les nombres ne sont pas corrects
			{
				erreur_bons_mauvais.value = true;
			}
			else { erreur_bons_mauvais.value = false; } //autrement 
			if (champs_non_remplis || erreur_bons_mauvais) {return;}

			axios.post('http://localhost:8000/api/tris/',{
				of:of.value,
				symbol:symbole.value,
				client:client.value,
				defaut:defaut.value,
				a_trier:a_trier.value,
				bonnes:bonnes.value,
				mauvaises:mauvaises.value,
				date:Date.now(),
				est_trie: est_trie.value,
			})
				.then(response=>{console.log(response)})
				.catch(err=>{console.log('err:' +err)})
			
		}

		console.log(data);


		return{
			postTri,

			of,
			symbole,
			client,
			defaut,
			a_trier,
			bonnes,
			mauvaises,
			est_trie,

			champs_non_remplis,
			erreur_bons_mauvais,

		}
	}
}
</script>

<style>
#container{
	display: flex;
	flex-direction: column;
	align-items: center;
	font-size: 45px;
}

#erreur-container{
	display: flex;
	flex-direction: column;
	align-items: center;
}

#erreur-champs{
	border: solid IndianRed;
	border-radius: 20px; 
	padding-left: 5px;
	padding-right: 5px;
	margin: 20px;
	background-color: #FFCCCC;
}

#erreur-champs p {
	color: red;
	margin: 10px;
}

#erreur-bons-mauvais{
	border: solid IndianRed;
	border-radius: 20px; 
	padding-left: 5px;
	padding-right: 5px;
	margin: 20px;
	background-color: #FFCCCC;
}

#erreur-bons-mauvais p {
	color: red;
	margin: 10px;
}

#post-tri-container {
	background-color: #EAEAEA;
	-webkit-box-shadow: 3px 4px 5px 3px rgba(0,0,0,0.75);
	-moz-box-shadow: 3px 4px 5px 3px rgba(0,0,0,0.75);
	box-shadow: 3px 4px 5px 3px rgba(0,0,0,0.75);
	width: 12em;
	display: flex;
	flex-direction: column;	
	justify-content: center;
	align-items: center;
}

#post-tri-container button {
	width: 100%;
	font-size: inherit;
}

.tri-input{
	width: 10em;
}

.tri-input-div{
	display: flex;
	flex-direction: row; 
	margin-top: 5px;
	gap: 2em;
}

.tri-label {
	width: 4em;
	padding-top: 5px;
	padding-bottom: 5px;
}

.tri-label:hover {
	background-color: lightgray;
}

</style>
