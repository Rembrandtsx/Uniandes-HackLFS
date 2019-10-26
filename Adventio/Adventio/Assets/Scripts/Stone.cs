using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Stone : MonoBehaviour
{
    public Route currentRoute;

    public GameObject prefab, dado1, dado2, dado3,dado4,dado5, dado6;

    
    int routePosition;

    int countOfSteps;
    public int steps;
    
    bool isMoving;
    

    void Start(){
        dado1.SetActive(false);
        dado2.SetActive(false);
        dado3.SetActive(false);
        dado4.SetActive(false);
        dado5.SetActive(false);
        dado6.SetActive(false);
    }
    void Update(){
        if((Input.GetKeyDown(KeyCode.Space)&& !isMoving)||( Input.GetMouseButtonDown(0) && !isMoving)){
            dado1.SetActive(false);
            dado2.SetActive(false);
            dado3.SetActive(false);
            dado4.SetActive(false);
            dado5.SetActive(false);
            dado6.SetActive(false);
            steps = Random.Range(1,7);
            if(steps == 1){
                dado1.SetActive(true);
            }else if(steps == 2){
                dado2.SetActive(true);
            }else if(steps == 3){
                dado3.SetActive(true);
                }
                else if(steps == 4){
                    dado4.SetActive(true);
                    }
                else if(steps == 5){
                    dado5.SetActive(true);
                    }
                else{
                    dado6.SetActive(true);
                    }
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
            countOfSteps++;
            if(countOfSteps >= currentRoute.childNodeList.Count * 3){
                Debug.Log("Final del Juego 3era Ronda");
            }
        }

        isMoving = false;
        Debug.Log(routePosition);
        play();
    }

    void play(){
        if(currentRoute.childNodeList[routePosition].gameObject.tag == "lab")
        {
            SceneManager.LoadScene("Laberynth", LoadSceneMode.Single);
            Debug.Log("Azul");
        }else{
            Debug.Log("Rojo");
        }
    }


    bool MoveToNextNode(Vector3 goal){
        return goal != (transform.position = Vector3.MoveTowards(transform.position, goal, 4f* Time.deltaTime));
    }
}
