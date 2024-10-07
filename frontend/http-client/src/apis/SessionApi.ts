/* tslint:disable */
/* eslint-disable */
/**
 * FarmNote
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: r206067@fhwn.ac.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  HTTPError,
  HTTPValidationError,
  Session,
} from '../models/index';
import {
    HTTPErrorFromJSON,
    HTTPErrorToJSON,
    HTTPValidationErrorFromJSON,
    HTTPValidationErrorToJSON,
    SessionFromJSON,
    SessionToJSON,
} from '../models/index';

export interface CreateSessionQrCodeRequest {
    token: string;
}

export interface JoinSessionRequest {
    token: string;
}

/**
 * 
 */
export class SessionApi extends runtime.BaseAPI {

    /**
     * Creates a new user session and returns a random token of 6 characters. This session has two purposes:                     <ol>                         <li>Group notes together. If all notes are read, only those with the matching token are displayed</li>                         <li>Used for authentication. Without a token, notes cannot be created, read, updated or deleted.</li>                     </ol>
     * Create Session
     */
    async createSessionRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Session>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SessionFromJSON(jsonValue));
    }

    /**
     * Creates a new user session and returns a random token of 6 characters. This session has two purposes:                     <ol>                         <li>Group notes together. If all notes are read, only those with the matching token are displayed</li>                         <li>Used for authentication. Without a token, notes cannot be created, read, updated or deleted.</li>                     </ol>
     * Create Session
     */
    async createSession(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Session> {
        const response = await this.createSessionRaw(initOverrides);
        return await response.value();
    }

    /**
     * Returns a QR code with a link to the web frontend to join an existing user session.
     * Get Session Qr Code
     */
    async createSessionQrCodeRaw(requestParameters: CreateSessionQrCodeRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<void>> {
        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling createSessionQrCode().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/qrcode`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Returns a QR code with a link to the web frontend to join an existing user session.
     * Get Session Qr Code
     */
    async createSessionQrCode(requestParameters: CreateSessionQrCodeRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<void> {
        await this.createSessionQrCodeRaw(requestParameters, initOverrides);
    }

    /**
     * Joins an existing user session. Returns status code 200 with all session notes if the token exists, otherwise 404.
     * Join Session
     */
    async joinSessionRaw(requestParameters: JoinSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Session>> {
        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling joinSession().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/join`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SessionFromJSON(jsonValue));
    }

    /**
     * Joins an existing user session. Returns status code 200 with all session notes if the token exists, otherwise 404.
     * Join Session
     */
    async joinSession(requestParameters: JoinSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Session> {
        const response = await this.joinSessionRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
