using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class collider : MonoBehaviour
{
  void OnCollisionEnter(Collision col){
      Debug.Log(gameObject.name + "Collided with: " + col.gameObject.name);
  }

}
