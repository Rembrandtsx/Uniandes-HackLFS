using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
public class collider : MonoBehaviour
{

    float levelTimer;
    bool updateTimer = true;

    public Text text;
    public GameObject oro, plata, bronce;

    
  void Start(){
      oro.SetActive(false);
      plata.SetActive(false);
      bronce.SetActive(false);

      levelTimer = 0.0f;
      Debug.Log("login Time"+ levelTimer);
  }
  void Update(){
    if (updateTimer){levelTimer += Time.deltaTime;}
  }
  void OnCollisionEnter(Collision col){
      updateTimer = false;
      Debug.Log(gameObject.name + "Collided with: " + col.gameObject.name + "Time Elapsed: " + levelTimer);
      if(levelTimer <= 23.5f){
          oro.SetActive(true);
      }else if(levelTimer>23.5f &&  levelTimer<=30.0f){
          plata.SetActive(true);
      }else {
          bronce.SetActive(true);
      }
      text.text = levelTimer + "S";
        WWWForm form = new WWWForm();
        form.AddField("usuario", "Juan");
        form.AddField("atributo2", levelTimer/1000 + "");
        form.AddField("atributo3", Random.Range(1,7) + "");
        form.AddField("juego", 1 + "");



        UnityWebRequest.Post("https://hackandes1.herokuapp.com/data", form);

  }

}
