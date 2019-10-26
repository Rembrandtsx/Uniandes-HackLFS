using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Stone : MonoBehaviour
{
    public Route currentRoute;

    public GameObject prefab;

    
    int routePosition;

    public int steps;
    
    bool isMoving;
    
    void Update(){
        if(Input.GetKeyDown(KeyCode.Space)&& !isMoving){
            steps = Random.Range(1,7);
            Debug.Log("El Dado es de:" + steps);
                StartCoroutine(Move());
            
        }
    }
    IEnumerator Move(){
        if(isMoving){
            yield break;
        }
        isMoving = true;

        while(steps>0){
            routePosition++;
            routePosition %= currentRoute.childNodeList.Count;

            Vector3 nextPos = currentRoute.childNodeList[routePosition].position;
            while(MoveToNextNode(nextPos)){
                
                Vector3 movement = new Vector3(nextPos.x,  0.0f, nextPos.y);
                prefab.transform.rotation = Quaternion.Slerp(prefab.transform.rotation, Quaternion.LookRotation(movement), 0.15F);
                

                yield return null;}
            
            yield return new WaitForSeconds(0.01f);
            steps--;
            
        }

        isMoving = false;
        Debug.Log(routePosition);
        play();
    }

    void play(){
        if(currentRoute.childNodeList[routePosition].gameObject.tag == "lab")
        {
            Debug.Log("Azul");
        }else{
            Debug.Log("Rojo");
        }
    }


    bool MoveToNextNode(Vector3 goal){
        return goal != (transform.position = Vector3.MoveTowards(transform.position, goal, 4f* Time.deltaTime));
    }
}
